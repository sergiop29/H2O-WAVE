from h2o_wave import ui, data, Q
from common import global_nav
from synthetic_data import *


async def show_red_dashboard(q: Q):
    q.page['meta'] = ui.meta_card(box='', layouts=[
        ui.layout(
            breakpoint='xs',
            width='1200px',
            zones=[
                ui.zone('header', size='76px'),
                ui.zone('title'),
                ui.zone('top', direction=ui.ZoneDirection.ROW, size='385px', zones=[
                    ui.zone('top_left'),
                    ui.zone('top_right', zones=[
                        ui.zone('top_right_top', direction=ui.ZoneDirection.ROW, size='1'),
                        ui.zone('top_right_bottom', size='1'),
                    ]),
                ]),
                ui.zone('middle', direction=ui.ZoneDirection.ROW, size='385px'),
                ui.zone('bottom', direction=ui.ZoneDirection.ROW, size='385px', zones=[
                    ui.zone('bottom_left'),
                    ui.zone('bottom_right', size='66%'),
                ]),
                ui.zone('footer', size='80px'),
            ]
        )
    ])

    q.page['header'] = ui.header_card(box='header', title='Tela Vermelha', subtitle='Dashboard de Marketing',
                                      image='https://wave.h2o.ai/img/h2o-logo.svg',
                                      items=[ui.tabs(name='Dashboards', value='#dashboards/red', 
                                                     items=global_nav),])
    q.page['title'] = ui.section_card(
        box='title',
        title='Performance de campanhas de Marketing',
        subtitle='Performance de campanhas de Marketing',
        items=[
            ui.label(label='Start:'),
            ui.date_picker(name='target_date1', label='', value='2020-12-20'),
            ui.label(label='End:'),
            ui.date_picker(name='target_date2', label='', value='2020-12-25'),
        ],
    )

    audience_days1 = generate_time_series(60)
    audience_days2 = generate_time_series(60)
    audience_hits1 = generate_random_walk(10000, 20000, 0.2)
    audience_hits2 = generate_random_walk(8000, 15000)

    q.page['audience_metrics'] = ui.form_card(
        box='top_left',
        title="Renda gerada pelas campanhas de Tráfego Pago",
        items=[
            ui.text('receita vinda das vendas de campanhas'),
            ui.stats(items=[
                ui.stat(label='Receita', value=next(sample_dollars)),
                ui.stat(label='KPI-A', value=next(sample_amount)),
                ui.stat(label='KPI-B', value=next(sample_amount)),
            ]),
            ui.visualization(
                plot=ui.plot([
                    ui.mark(type='area', x_scale='time', x='=date', y='=visitors', color='=site',
                            color_range='$red $tangerine'),
                    ui.mark(type='line', x_scale='time', x='=date', y='=visitors', color='=site',
                            color_range='$red $tangerine'),
                ]),
                data=data(
                    fields=['site', 'date', 'visitors'],
                    rows=[('A', next(audience_days1), next(audience_hits1)) for i in range(60)] + [
                        ('B', next(audience_days2), next(audience_hits2)) for i in range(60)],
                    pack=True
                ),
                height='210px',
            )
        ],
    )

    bounce_days = generate_time_series(30)
    bounce_rates = generate_random_walk()
    q.page['bounce_rate'] = ui.tall_series_stat_card(
        box='top_right_top',
        title='Devoluções Médias por pedido',
        value=next(sample_amount),
        aux_value='',
        plot_type='area',
        plot_color='$red',
        plot_category='date',
        plot_value='bounce_rate',
        plot_zero_value=0,
        plot_data=data(
            fields=['date', 'bounce_rate'],
            rows=[(next(bounce_days), next(bounce_rates)) for i in range(30)],
            pack=True,
        ),
    )

    user_days = generate_time_series(30)
    user_counts = generate_random_walk()
    q.page['total_users'] = ui.tall_series_stat_card(
        box='top_right_top',
        title='Valor de Devoluções',
        value=next(sample_dollars),
        aux_value='',
        plot_type='interval',
        plot_color='$tangerine',
        plot_category='date',
        plot_value='users',
        plot_zero_value=0,
        plot_data=data(
            fields=['date', 'users'],
            rows=[(next(user_days), next(user_counts)) for i in range(20)],
            pack=True,
        ),
    )

    session_days = generate_time_series(60)
    session_counts = generate_random_walk()
    q.page['all_sessions'] = ui.tall_series_stat_card(
        box='top_right_bottom',
        title='Quantidade de Usuários',
        value='18.976 Usuários únicos',
        aux_value='ada usuário que visitou nosso site, pelo menos uma vez',
        plot_type='interval',
        plot_color='$red',
        plot_category='date',
        plot_value='users',
        plot_zero_value=0,
        plot_data=data(
            fields=['date', 'users'],
            rows=[(next(session_days), next(session_counts)) for i in range(60)],
            pack=True,
        ),
    )

    q.page['page_views'] = ui.stat_list_card(
        box='middle',
        title='Desempenho de Campanhas',
        subtitle=next(sample_caption),
        items=[
            ui.stat_list_item(label=next(sample_title), caption=next(sample_caption), value=next(sample_dollars),
                              aux_value=next(sample_term), value_color=next(sample_color)) for i in range(5)
        ],
    )

    session_count = generate_random_walk(1000, 8000)
    session_source = generate_sequence(['Search', 'Email', 'Referral', 'Social', 'Other'])

    q.page['dist_by_channel'] = ui.plot_card(
        box='middle',
        title='Meios de prospecção',
        data=data(
            fields=['site', 'channel', 'sessions'],
            rows=[('A', next(session_source), next(session_count)) for i in range(5)] + [
                ('B', next(session_source), next(session_count)) for i in range(5)],
            pack=True,
        ),
        plot=ui.plot([
            ui.mark(coord='theta', type='interval', x='=site', y='=sessions', color='=channel', stack='auto', y_min=0,
                    color_range='$amber $orange $tangerine $red $pink')
        ])
    )
    q.page['sessions_by_channel'] = ui.plot_card(
        box='middle',
        title='Visitas por canal',
        data=data(
            fields=['channel', 'sessions'],
            rows=[(next(sample_term), next(session_count)) for i in range(10)],
            pack=True,
        ),
        plot=ui.plot([
            ui.mark(type='interval', x='=sessions', y='=channel', y_min=0, color='$red')
        ])
    )

    q.page['acquisitions'] = ui.form_card(
        box='bottom_left',
        title='Categoria de Produtos vendidos',
        items=[
            ui.text('Quantidade vendida na categoria / Total de Produtos vendidos'),
            ui.stats(items=[
                ui.stat(label=next(sample_term), value=next(sample_percent), icon=next(sample_icon),
                        icon_color=next(sample_color)),
                ui.stat(label=next(sample_term), value=next(sample_percent), icon=next(sample_icon),
                        icon_color=next(sample_color)),
            ]),
        ],
    )
    q.page['sessions'] = ui.form_card(
        box='bottom_left',
        title='Produtos com Maiores Margens',
        items=[
            ui.text('Margem Bruta por Produto'),
            ui.stats(items=[
                ui.stat(label=next(sample_term), value=next(sample_percent), icon=next(sample_icon),
                        icon_color=next(sample_color)),
                ui.stat(label=next(sample_term), value=next(sample_percent), icon=next(sample_icon),
                        icon_color=next(sample_color)),
            ]),
        ],
    )
    q.page['pages'] = ui.stat_table_card(
        box='bottom_right',
        title='Perfomance de campanhas',
        subtitle='Resultados de campanhas para cada público alvo',
        columns=['Campanha', 'Receita Gerada', 'Margem Bruta', 'Evolução de Resultados'],
        items=[
            ui.stat_table_item(label=next(sample_term), caption=next(sample_title),
                               values=[next(sample_dollars), next(sample_percent), next(sample_percent)],
                               icon=next(sample_icon), icon_color=next(sample_color)) for i in range(5)
        ]
    )

    q.page['footer'] = ui.footer_card(box='footer', caption='(c) 2021 Bravonix. All rights reserved.')

    await q.page.save()
