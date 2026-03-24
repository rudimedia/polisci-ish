from datetime import datetime
from nicegui import ui

abstract_morning = """In an audacious attempt to decipher the enigma of political polarization
that has engulfed contemporary democratic societies..."""

abstract_noon = """The escalating rift between ideological extremes within political systems..."""

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

  .abstract-text {
    text-align: justify;
    line-height: 1.7;
    hyphens: auto;
    overflow-wrap: break-word;
  }

  .doi {
    margin-top: 1.5rem;
    font-size: 0.8rem;
    color: #777;
  }
</style>
''')

def get_text():
    now = datetime.now()
    current_hm = now.strftime('%H:%M')

    if current_hm >= '12:35' or current_hm < '07:00':
        return abstract_noon
    else:
        return abstract_morning

def get_date():
    return datetime.now().strftime('%Y-%m-%d')

with ui.element('div').classes('center-wrap'):
    with ui.element('div').classes('abstract-box'):

        # Header (title left, date right)
        with ui.element('div').classes('header'):
            ui.label('Article about bees and beans').classes('title')
            date_label = ui.label(get_date()).classes('date')

        # Abstract
        abstract_label = ui.markdown(get_text()).classes('abstract-text')

        # DOI (bottom)
        ui.label('DOI: 10.1234/example.doi').classes('doi')

def update_text():
    abstract_label.set_content(get_text())
    date_label.set_text(get_date())

ui.timer(30.0, update_text)

ui.run()