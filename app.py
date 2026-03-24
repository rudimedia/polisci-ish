from nicegui import ui


text = "hallo"

ui.add_head_html('''
<style>
  .center-wrap {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .hero-text {
    font-size: 2rem;
    font-weight: 600;
    text-align: left;
  }
</style>
''')

with ui.element('div').classes('center-wrap'):
    ui.html(f'<div class="text">{text}<br><i>formatted</i> text</div>')

ui.run()