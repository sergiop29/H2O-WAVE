from h2o_wave import main, app, Q

from pages.dashboard_JP_ocupacao_UPA import show_ocup_upa
from pages.dashboard_red import show_red_dashboard
from pages.dashboard_blue import show_blue_dashboard
from pages.dashboard_orange import show_orange_dashboard
from pages.dashboard_cyan import show_cyan_dashboard
from pages.dashboard_grey import show_grey_dashboard
from pages.dashboard_mint import show_mint_dashboard
from pages.dashboard_purple import show_purple_dashboard

@app('/dash')
async def serve(q: Q):
    route = q.args['#']
    q.page.drop()
    if route == 'dashboards/UPA':
        await show_ocup_upa(q)
    elif route == 'dashboards/red':
        await show_red_dashboard(q)
    elif route == 'dashboards/blue':
        await show_blue_dashboard(q)
    elif route == 'dashboards/orange':
        await show_orange_dashboard(q)
    elif route == 'dashboards/cyan':
        await show_cyan_dashboard(q)
    elif route == 'dashboards/grey':
        await show_grey_dashboard(q)
    elif route == 'dashboards/mint':
        await show_mint_dashboard(q)
    elif route == 'dashboards/purple':
        await show_purple_dashboard(q)
    else:
        await show_ocup_upa(q)