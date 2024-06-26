from h2o_wave import Q, main, app, ui, site, data
import pandas as pd

@app('/dash')
async def serve(q):
    if not q.client.initialized:
        set_up_ui_for_new_user(q)
    elif q.args.table:
        table_view(q)
    elif q.args.plot:
        plot_view(q)
    elif (q.args.x_variable is not None) or (q.args.y_variable is not None):
        q.client.x_variable = q.args.x_variable
        q.client.y_variable = q.args.y_variable
        plot_view(q)

    await q.page.save()

    def set_up_ui_for_new_user(q):
        q.page['meta'] = ui.meta_card(
            box="",
            layouts=[
                ui.layout(
                    breakpoints="xs",
                    zones=[
                        ui.zone("header"),
                        ui.zone("navigation"),
                        ui.zone("content")
                    ]
                )
            ]
        )

        q.page["header"] = ui.header_card(
            box="header",
            title="Titulo da Pagina",
            subtitle="Texto de subtitulo"
        )

        q.page["navigation"] = ui.tab_card(
            box="navigation",
            items=[
                ui.tab(name="table", label="Table View"),
                ui.tab(name="plot", label="Plot View"),
            ]
        )

        q.client.x_variable = 'Data_de_Venda'
        q.client.y_variable = 'Valor_Bruto'
        q.client.initialized = True

    await q.page.save()

def table_view(q):
    del q.page["plot_view"]

    df = aggregated_data()

    q.page["table_view"] = ui.form_card(
        box = "content",
        items=[
            ui.text_xl("Table View"),
            ui.table(
                name="aggregated_data_table",
                columns=[ui.table_column(name=col, label=col) for col in df.columns.values],
                rows=[
                    ui.table_row(
                        name=str(i),
                        cells=[str(df[col].values) for col in df.columns.values]
                    ) for i in range(len(df))
                ], downloadable=True
            )
        ]
    )

def plot_view(q):
    del q.page["table_view"]
    df = aggregated_data()

    q.page["plot_view"] = ui.form_card(
        box = "content",
        items=[
            ui.text_xl(f"Relação entre {q.client.x_variable} e {q.client.y_variable}"),
            ui.inline(
                items=[
                    ui.dropdown(
                        name='x_variable', 
                        label='x variable', 
                        choices= [
                            ui.choice(name=col, label=col) for col in df.columns.values
                            ], trigger=True, value=q.client.x_variable
                    ),
                    ui.dropdown(
                        name='y_variable', 
                        label='y variable', 
                        choices= [
                            ui.choice(name=col, label=col) for col in df.columns.values
                            ], trigger=True, value=q.client.y_variable
                    ),
                ]
            ),
            ui.visualization(
                data=data(
                    fields=df.columns.tolist(),
                    rows=df.values.tolist(),
                    pack=True, #como não terá atualização constante, essa config otimiza o uso de memória
                ),
                plot=ui.plot(
                        marks=[
                            ui.mark(
                                type='point', #scatterplot
                                x=f'{q.client.x_variable}', x_title='',
                                y=f'{q.client.y_variable}', y_title='',
                                # color='=data_type', 
                                shape='circle',
                                size='counts'
                        )
                    ]
                )
            )
        ]
    )

def aggregated_data():
    df = pd.read_excel('Base de Dados Workshop.xlsx')
    print(df.head())
    return df