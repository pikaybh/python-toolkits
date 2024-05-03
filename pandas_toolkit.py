import pandas as pd


def save_df(df : pd.DataFrame, file : str) -> None:
    """
    save data frame easy.
    :param df: Target DF
    :type df: pd.DataFrame
    :param file: Target file name. (Must contain extension)
    :type file: str
    :return: None
    """
    ext = file.split('.')[-1]
    if ext == "csv":
        df.to_csv(file, index=False, encoding='utf-8-sig')
    elif ext == "xlsx":
        df.to_excel(file, index=False)
    else:
        raise ValueError(f".{ext} is not supported. ({ext = })")