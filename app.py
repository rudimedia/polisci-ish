from datetime import datetime, time
from nicegui import ui
import pandas as pd
import ast

data = pd.read_csv("data/clean_abstracts.csv")

abstract_morning = data.iloc[99]
abstract_noon = data.iloc[50]

ui.add_head_html('''
<style>
  .center-wrap {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: clamp(1rem, 4vw, 3rem);
    box-sizing: border-box;
  }

  .abstract-box {
    width: min(100%, 900px);
    padding: clamp(1rem, 4vw, 2.5rem);
    box-sizing: border-box;
    background: white;
    border-radius: 12px;
  }

  .header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 1rem;
    gap: 1rem;
  }

  .title {
    font-size: 1.4rem;
    font-weight: 600;
  }

  .date {
    font-size: 0.9rem;
    color: #666;
    white-space: nowrap;
  }

    .abstract-box {
    width: min(100%, 900px);
    padding: clamp(1rem, 4vw, 2.5rem);
    box-sizing: border-box;
    background: white;
    border-radius: 12px;

    display: flex;
    flex-direction: column;   /* stack vertically */
    height: 100%;
    }

    .abstract-text {
    text-align: justify;
    line-height: 1.7;
    hyphens: auto;
    overflow-wrap: break-word;

    flex-grow: 1;  /* pushes citation downward */
    }

    .doi {
    margin-top: 0.5rem;
    font-size: 0.8rem;
    color: #777;
    max-width: 70%;
    align-self: flex; 
    text-align: left;
    }
</style>
''')

def get_text():
    now = datetime.now().time()
    if now >= time(12, 35) or now < time(7, 0):
        return abstract_noon
    return abstract_morning
    
current = get_text()

with ui.element('div').classes('center-wrap'):
    with ui.element('div').classes('abstract-box'):

        with ui.element('div').classes('header'):
            title_label = ui.label().classes('title')
            citations = ui.label().classes("date")

        abstract_label = ui.markdown().classes('abstract-text')
        citation_block = ui.markdown().classes('doi')
        

def update_text():
    current = get_text()
    citations.set_text(f"Citations: {current["ref_count"]}")
    title_label.set_text(current["title"])
    abstract_label.set_content(current["abstract"])
    citation_block.set_content(current["apa_citation"])

ui.timer(30.0, update_text)

ui.run()
