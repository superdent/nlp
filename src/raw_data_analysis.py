"""
Explorative Datenanalyse (EDA) für Sentimentanalyse-Projekt
Erzeugt einen Markdown-Report mit PNG-Grafiken in einem Unterordner
"""

import json
import gc
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def count_lines(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)


def load_jsonl_reviews(filepath, max_records=None):
    records = []

    with open(filepath, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if max_records and i >= max_records:
                break

            if i > 0 and i % 10_000_000 == 0:
                print(f"  {i:,} Datensätze gelesen – {datetime.now().strftime('%H:%M:%S')}")

            try:
                record = json.loads(line)
                item = {
                    'title': record.get('title') or record.get('summary') or '',
                    'text': record.get('text') or record.get('body') or record.get('review_text') or '',
                    'rating': record.get('rating') or record.get('overall')
                }
                records.append(item)
            except json.JSONDecodeError:
                continue

    print(f"  {len(records):,} Datensätze gelesen – {datetime.now().strftime('%H:%M:%S')}")
    return pd.DataFrame(records)


def analyze_category(cat_name, filepath, max_records=5_000_000):
    """Analysiert eine Kategorie"""
    print(f"► Analysiere {cat_name}...")

    df = load_jsonl_reviews(filepath, max_records=max_records)

    text_lengths = df['text'].str.len()
    title_lengths = df['title'].str.len()
    word_counts = df['text'].str.split().str.len()
    rating_counts = df['rating'].value_counts().sort_index()

    stats = {
        'category': cat_name,
        'total_records': len(df),
        'text_length_mean': text_lengths.mean(),
        'text_length_std': text_lengths.std(),
        'text_length_min': text_lengths.min(),
        'text_length_max': text_lengths.max(),
        'title_length_mean': title_lengths.mean(),
        'word_count_mean': word_counts.mean(),
        'null_title': df['title'].isnull().sum(),
        'null_text': df['text'].isnull().sum(),
        'null_rating': df['rating'].isnull().sum(),
        'rating_1': rating_counts.get(1, 0),
        'rating_2': rating_counts.get(2, 0),
        'rating_3': rating_counts.get(3, 0),
        'rating_4': rating_counts.get(4, 0),
        'rating_5': rating_counts.get(5, 0),
    }

    return df, stats


def create_and_save_plots(df, cat_name, figures_dir):
    """Erstellt und speichert Diagramme für Bewertungen und Textlängen"""

    fig, ax = plt.subplots(figsize=(8, 5))
    rating_counts = df['rating'].value_counts().sort_index()
    ax.bar(rating_counts.index, rating_counts.values, color='steelblue', edgecolor='black')
    ax.set_xlabel('Bewertung', fontsize=11)
    ax.set_ylabel('Anzahl', fontsize=11)
    ax.set_title(f'Verteilung der Bewertungen: {cat_name}', fontsize=12, fontweight='bold')
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.grid(axis='y', alpha=0.3)

    rating_filename = f"{cat_name.replace(' ', '_')}_rating.png"
    rating_path = figures_dir / rating_filename
    fig.savefig(rating_path, dpi=100, bbox_inches='tight')
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 5))
    text_lengths = df['text'].str.len()
    ax.hist(text_lengths, bins=50, color='coral', edgecolor='black', alpha=0.7)
    ax.set_xlabel('Textlänge (Zeichen)', fontsize=11)
    ax.set_ylabel('Häufigkeit', fontsize=11)
    ax.set_title(f'Verteilung der Textlängen: {cat_name}', fontsize=12, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)

    textlen_filename = f"{cat_name.replace(' ', '_')}_textlen.png"
    textlen_path = figures_dir / textlen_filename
    fig.savefig(textlen_path, dpi=100, bbox_inches='tight')
    plt.close(fig)

    return rating_filename, textlen_filename


def generate_markdown_report(all_stats, all_plot_files, figures_dirname):
    """Erzeugt einen Markdown-Report mit Links zu PNG-Grafiken"""
    print("► Erzeuge Markdown-Report...")

    md = []
    md.append("# EDA-Report: Sentimentanalyse")
    md.append("")
    md.append("Amazon-Reviews aus 4 Produktkategorien")
    md.append("")

    md.append("## Übersichtstabelle")
    md.append("")

    summary_rows = []
    for stat in all_stats:
        summary_rows.append({
            'Kategorie': stat['category'],
            'Datensätze (Rohdatei)': f"{stat['total_records_raw']:,}",
            'Datensätze (analysiert)': f"{stat['total_records']:,}",
            'Ø Textlänge': f"{stat['text_length_mean']:.0f}",
            'Ø Wörter': f"{stat['word_count_mean']:.0f}",
            'Bewertung 1': stat['rating_1'],
            'Bewertung 5': stat['rating_5'],
        })

    df_summary = pd.DataFrame(summary_rows)
    md.append(df_summary.to_markdown(index=False))
    md.append("")
    md.append("---")
    md.append("")

    for stats in all_stats:
        cat_name = stats['category']
        rating_file, textlen_file = all_plot_files[cat_name]

        md.append(f"## {cat_name}")
        md.append("")

        md.append("### Statistiken")
        md.append(f"- **Datensätze in Rohdatei:** {stats['total_records_raw']:,}")
        md.append(f"- **Davon analysiert:** {stats['total_records']:,}")
        md.append(f"- **Fehlende Werte:** title={stats['null_title']}, text={stats['null_text']}, rating={stats['null_rating']}")
        md.append("")

        md.append("### Verteilung der Bewertungen")
        for i in range(1, 6):
            count = stats[f'rating_{i}']
            pct = count / stats['total_records'] * 100
            md.append(f"- **{i} Sterne:** {count:,} ({pct:.1f}%)")
        md.append("")

        md.append("### Textlänge (Zeichen)")
        md.append("| Kennzahl | Wert |")
        md.append("|--------|-------|")
        md.append(f"| Mittelwert | {stats['text_length_mean']:.0f} |")
        md.append(f"| Standardabweichung | {stats['text_length_std']:.0f} |")
        md.append(f"| Minimum | {stats['text_length_min']:.0f} |")
        md.append(f"| Maximum | {stats['text_length_max']:.0f} |")
        md.append(f"| Durchschnittliche Wortanzahl | {stats['word_count_mean']:.0f} |")
        md.append("")

        md.append("### Diagramm: Bewertungsverteilung")
        md.append(f"![Bewertungsverteilung]({figures_dirname}/{rating_file})")
        md.append("")

        md.append("### Diagramm: Verteilung der Textlängen")
        md.append(f"![Textlänge]({figures_dirname}/{textlen_file})")
        md.append("")

        md.append("---")
        md.append("")

    md.append("## Zentrale Erkenntnisse")
    md.append("")
    md.append("### Eigenschaften der Kategorien")

    largest = max(all_stats, key=lambda x: x['total_records_raw'])
    longest_text = max(all_stats, key=lambda x: x['text_length_mean'])
    longest_words = max(all_stats, key=lambda x: x['word_count_mean'])

    md.append(f"- **Größter Datensatz:** {largest['category']} ({largest['total_records_raw']:,} Datensätze)")
    md.append(f"- **Längste Texte:** {longest_text['category']} (Ø {longest_text['text_length_mean']:.0f} Zeichen)")
    md.append(f"- **Meiste Wörter:** {longest_words['category']} (Ø {longest_words['word_count_mean']:.0f} Wörter)")
    md.append("")

    md.append("### Balance der Bewertungen")
    for stat in all_stats:
        total = stat['total_records']
        rating_1_pct = stat['rating_1'] / total * 100
        rating_5_pct = stat['rating_5'] / total * 100
        md.append(f"- **{stat['category']}:** {rating_1_pct:.1f}% negativ (1 Stern), {rating_5_pct:.1f}% positiv (5 Sterne)")
    md.append("")

    return "\n".join(md)


if __name__ == "__main__":

    categories = {
        'Movies & TV': 'data/raw/Movies_and_TV.jsonl',
        'All Beauty': 'data/raw/All_Beauty.jsonl',
        'Office Products': 'data/raw/Office_Products.jsonl',
        'Books': 'data/raw/Books.jsonl'
    }

    doc_dir = Path('documentation')
    doc_dir.mkdir(parents=True, exist_ok=True)

    figures_dirname = 'phase1_eda_report_figures'
    figures_dir = doc_dir / figures_dirname
    figures_dir.mkdir(parents=True, exist_ok=True)

    print("\n" + "="*60)
    print("EXPLORATIVE DATENANALYSE")
    print("="*60 + "\n")

    all_stats = []
    all_plot_files = {}
    total_counts = {}

    print("► Zähle Datensätze in Rohdateien...")
    for cat_name, filepath in categories.items():
        count = count_lines(filepath)
        total_counts[cat_name] = count
        print(f"  {cat_name}: {count:,}")
    print()

    for cat_name, filepath in categories.items():
        df, stats = analyze_category(cat_name, filepath, max_records=5_000_000)
        stats['total_records_raw'] = total_counts[cat_name]
        rating_file, textlen_file = create_and_save_plots(df, cat_name, figures_dir)

        all_stats.append(stats)
        all_plot_files[cat_name] = (rating_file, textlen_file)

        del df
        gc.collect()
        print(f"  Speicher freigegeben für {cat_name}\n")

    report_md = generate_markdown_report(all_stats, all_plot_files, figures_dirname)

    report_path = doc_dir / '1_eda_result.md'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_md)

    print(f"\n✓ Report gespeichert unter: {report_path}")
    print(f"✓ Grafiken gespeichert unter: {figures_dir}")
    print("="*60 + "\n")