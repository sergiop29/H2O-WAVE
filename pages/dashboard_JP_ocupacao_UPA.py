from h2o_wave import ui, data, Q
from common import global_nav
from synthetic_data import *

async def show_ocup_upa(q: Q):
    q.page['meta'] = ui.meta_card(box='', layouts=[
        ui.layout(
            breakpoint='xs',
            width='1200px',
            zones=[
                ui.zone('header', size='76px'),
                ui.zone('body', size='900px', direction=ui.ZoneDirection.ROW, zones=[
                    ui.zone('sidebar', size='18%'),
                    ui.zone('content', size='82%', zones=[
                        ui.zone('title', size='60px'),
                        ui.zone('top', size='150px', direction=ui.ZoneDirection.ROW, zones=[
                            ui.zone('top_left'),
                            ui.zone('top_mid'),
                            ui.zone('top_mid_2'),
                            ui.zone('top_right'),
                        ]),
                        ui.zone('middle', size='400px'),
                        ui.zone('bottom', size='275px', direction=ui.ZoneDirection.ROW, zones=[
                            ui.zone('bot_left', size='35%'),
                            ui.zone('bot_mid'),
                            ui.zone('bot_right'),
                        ])
                    ]),
                ]),
                ui.zone('footer', size='80px'),
            ]
        )
    ])

    #Header da página
    q.page['header'] = ui.header_card(box='header', title='João Pessoa | Análise de ocupação em UPAs', subtitle='Dashboard criado pela LGPDNOW',
                                      image='assets/lgpd_logo_verde.png',
                                      items=[ui.tabs(name='Dashboards', value='#JP/UPA', 
                                                     items=global_nav),
                                                     ]
                                        )
    q.page['section'] = ui.section_card(
        box=ui.box('title', order=1, size=0),
        title='Filtre as informações conforme desejar!',
        subtitle='Use a barra lateral para utilizar os filtros, juntamente com o filtro de datas à direita',
        items=[
            ui.date_picker(name='target_date', label='', value='2020-12-25'),
        ],
    )
    q.page['filter-0'] = ui.form_card(
        box=ui.box('sidebar', height='115px', order=2),
        title='Ano',
        items=[
            ui.separator(label=''),
            ui.date_picker(name='target_date', label='', value='2020-12-25'),
        ],
    )
    q.page['filter-1'] = ui.form_card(
        box=ui.box('sidebar', height='250px', order=2),
        title='Atendimentos',
        items=[
            ui.separator(label=''),
            ui.dropdown(name='region', label='Unidades', value='option0', choices=[
                ui.choice(name=f'option{i}', label=next(sample_term)) for i in range(5)
            ]),
            ui.text(''),
            ui.text(''),
            ui.dropdown(name='age', label='Especialidades', value='option0', choices=[
                ui.choice(name=f'option{i}', label=next(sample_term)) for i in range(5)
            ]),
        ],
    )
    q.page['filter-2'] = ui.form_card(
        box=ui.box('sidebar', height='300px', order=2),
        title='Paciente',
        items=[
            ui.separator(label=''),
            ui.dropdown(name='region', label='Origem', value='option0', choices=[
                ui.choice(name=f'option{i}', label=next(sample_term)) for i in range(5)
            ]),
            ui.text(''),
            ui.text(''),
            ui.dropdown(name='age', label='Idade', value='option0', choices=[
                ui.choice(name=f'option{i}', label=next(sample_term)) for i in range(5)
            ]),
            ui.text(''),
            ui.text(''),
            ui.button(name='limpar', label='Limpar filtros',
                    #   commands=[]
                      )
        ],
    )
    # Retirar quando tiver os dados
    customers_overview_dates = generate_time_series(30)
    customers_overview_counts = generate_random_walk()
    q.page['card-atendimentos'] = ui.tall_series_stat_card(
        box=ui.box('top_left'),
        title='Atendimentos',
        value=next(sample_dollars),
        aux_value='',
        plot_type='area',
        plot_color='$green',
        plot_category='date',
        plot_value='customer_count',
        plot_zero_value=0,
        plot_data=data(
            fields=['date', 'customer_count'],
            rows=[(next(customers_overview_dates), next(customers_overview_counts)) for i in range(30)],
            pack=True,
        ),
    )
    q.page['card-media'] = ui.tall_series_stat_card(
        box=ui.box('top_mid'),
        title='Média de Idade',
        value=next(sample_dollars),
        aux_value='',
        plot_type='area',
        plot_color='$green',
        plot_category='date',
        plot_value='customer_count',
        plot_zero_value=0,
        plot_data=data(
            fields=['date', 'customer_count'],
            rows=[(next(customers_overview_dates), next(customers_overview_counts)) for i in range(30)],
            pack=True,
        ),
    )
    q.page['card-especialidade'] = ui.tall_series_stat_card(
        box=ui.box('top_mid_2'),
        title='Especialidade',
        value=next(sample_dollars),
        aux_value='',
        plot_type='area',
        plot_color='$green',
        plot_category='date',
        plot_value='customer_count',
        plot_zero_value=0,
        plot_data=data(
            fields=['date', 'customer_count'],
            rows=[(next(customers_overview_dates), next(customers_overview_counts)) for i in range(30)],
            pack=True,
        ),
    )
    q.page['card-especialistas'] = ui.tall_series_stat_card(
        box=ui.box('top_right'),
        title='Especialistas',
        value=next(sample_dollars),
        aux_value='',
        plot_type='area',
        plot_color='$green',
        plot_category='date',
        plot_value='customer_count',
        plot_zero_value=0,
        plot_data=data(
            fields=['date', 'customer_count'],
            rows=[(next(customers_overview_dates), next(customers_overview_counts)) for i in range(30)],
            pack=True,
        ),
    )
    q.page['line_chart'] = ui.plot_card(
    box=ui.box('middle', order=1),
    title='Quantidade de Atendimentos',
    data=data('month city temperature', 24, rows=[
        ('Jan', 'Bancários', 7),
        ('Jan', 'Valentina', 3.9),
        ('Feb', 'Bancários', 6.9),
        ('Feb', 'Valentina', 4.2),
        ('Mar', 'Bancários', 9.5),
        ('Mar', 'Valentina', 5.7),
        ('Apr', 'Bancários', 14.5),
        ('Apr', 'Valentina', 8.5),
        ('May', 'Bancários', 18.4),
        ('May', 'Valentina', 11.9),
        ('Jun', 'Bancários', 21.5),
        ('Jun', 'Valentina', 15.2),
        ('Jul', 'Bancários', 25.2),
        ('Jul', 'Valentina', 17),
        ('Aug', 'Bancários', 26.5),
        ('Aug', 'Valentina', 16.6),
        ('Sep', 'Bancários', 23.3),
        ('Sep', 'Valentina', 14.2),
        ('Oct', 'Bancários', 18.3),
        ('Oct', 'Valentina', 10.3),
        ('Nov', 'Bancários', 13.9),
        ('Nov', 'Valentina', 6.6),
        ('Dec', 'Bancários', 9.6),
        ('Dec', 'Valentina', 4.8),
        ]),
    plot=ui.plot([
        ui.mark(type='line', x='=month', y='=temperature', color='=city', y_min=0,
                label='={{intl temperature minimum_fraction_digits=1 maximum_fraction_digits=1}}'
                )
        ])
    )
    q.page['pie_chart'] = ui.wide_pie_stat_card(
    box=ui.box('bot_left', order=1),
    title='Sexo dos Pacientes',
    pies=[
        ui.pie(label='Masculino', value='41,07%', fraction=0.4107, color='$green', aux_value='$ 122'),
        ui.pie(label='Feminino', value='58,93%', fraction=0.5893, color='$red', aux_value='$ 160'),
    ]
    )
    session_count = generate_random_walk(10, 1000)
    q.page['sessions_by_channel'] = ui.plot_card(
        box=ui.box('bot_mid', order=1),
        title='Origem dos Usuários',
        data=data(
            fields=['channel', 'sessions'],
            rows=[(next(sample_term), next(session_count)) for i in range(5)],
            pack=True,
        ),
        plot=ui.plot([
            ui.mark(type='interval', x='=sessions', y='=channel', y_min=0, color='$green')
        ])
    )

    q.page['sessions_by_channel_'] = ui.plot_card(
        box=ui.box('bot_right', order=1),
        title='Atendimentos por CID',
        data=data(
            fields=['channel', 'sessions'],
            rows=[(next(sample_term), next(session_count)) for i in range(5)],
            pack=True,
        ),
        plot=ui.plot([
            ui.mark(type='interval', x='=sessions', y='=channel', y_min=0, color='#B5F7DB')
        ])
    )
    q.page['footer'] = ui.footer_card(box='footer', caption='(c) 2024 LGPDNOW. All rights reserved.')

    await q.page.save()