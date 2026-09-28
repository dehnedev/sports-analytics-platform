def build_features(df):
    df['score_diff'] = df['home_score'] - df['away_score']

    X = df[
        [
            'score_diff',
            'home_win_pct',
            'away_win_pct',
            'is_home',
            'home_point_diff_last3',
            'away_point_diff_last3',
        ]
    ]

    y = df['home_win']
    return X, y
