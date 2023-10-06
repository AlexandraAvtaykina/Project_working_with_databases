from config import config
from classes import DBManager
from utils import get_hhru_data, create_database, save_data_to_database


def main():
    employer_ids = [
        '1753496',  # ООО Бизапс
        '1795330',  # Ateuco
        '2751250',  # AdminDivision
        '1975782',  # ООО 101
        '669853',  # BeFresh
        '2450307',  # ООО АльянсТелекоммуникейшнс
        '10170495',  # ООО 20 тонн
        '3446179',  # Gembo
        '5536919',  # Come&Pass
        '193400',  # АВТОВАЗ
    ]
    params = config()

    data = get_hhru_data(employer_ids)

    create_database('hhru', params)
    save_data_to_database(data, 'hhru', params)


if __name__ == '__main__':
    main()
