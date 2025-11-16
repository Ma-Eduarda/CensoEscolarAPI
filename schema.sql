CREATE TABLE IF NOT EXISTS tb_instituicao (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT NOT NULL,
        nome TEXT NOT NULL,
        co_uf INTEGER NOT NULL,
        co_municipio INTEGER NOT NULL,
        qt_mat_bas INTEGER NOT NULL,
        qt_mat_prof INTEGER NOT NULL,
        qt_mat_eja INTEGER NOT NULL,
        qt_mat_esp INTEGER NOT NULL
);

