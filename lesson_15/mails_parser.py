import csv
import json
import re
import logging
import os

CATEGORIES = ("Security", "Refunds", "Troubleshooting", "Account", "Advertising_and_Collaboration",
              "Limits", "Payments", "Features", "Others")
file_name = "user_support_letters.csv"
result_file = "result.csv"
LOG_FORMAT = "{levelname:<8} - {asctime}: {msg}"
if not os.path.isdir("logs"):
    os.mkdir("logs")
logging.basicConfig(filename=os.path.join("logs", "segreg.log"), format=LOG_FORMAT, style="{", level=logging.NOTSET)
logger = logging.getLogger("Segregator log")


class MailSegregator:
    __knowledge_file = "knowledge.json"
    """
    This class takes csv file with unsorted mails and segregates they to named csv files.
    In initialization takes categories of mails.
    """

    def __init__(self, name: str = "Sorter", *args, **kwargs):
        self.name = name
        self.list_of_mails = []
        try:
            with open(self.__knowledge_file, encoding="utf-8") as knowledge:
                self.knowledge = json.load(knowledge)
        except FileNotFoundError:
            logger.error(f"not found a file to learning ({self.__knowledge_file})")
            self.knowledge = {}
        self.categories = {}
        if args:
            for arg in args:
                self.categories[arg] = []
        if kwargs:
            for key, value in kwargs:
                self.categories[value] = []
        logger.info(f"initialization of sorter '{self.name}' is completed")

    def write_to_knowledge(self):
        """Writes own knowledge to knowledge file."""
        with open(self.__knowledge_file, "w", encoding="utf-8") as knowledge_file:
            json.dump(self.knowledge, knowledge_file, indent=4, ensure_ascii=False)
        logger.info(f"Knowledge of sorter '{self.name}' is writing to file {self.__knowledge_file}")

    def read_mails_file(self, filename: str):
        """Reads from csv file mails and writes all mails to list."""
        try:
            with open(filename, encoding="utf-8") as csv_file:
                reader = csv.reader(csv_file)
                self.list_of_mails = [mail[0] for mail in reader]
                logger.info(f"The sorter '{self.name}' read mails from file {file_name}")
        except FileNotFoundError:
            logger.error(f"The file {file_name} not founded")
        except Exception as e:
            logger.error(f"Problem with file {file_name}: {e}")

    def write_result_to_file(self, filename: str):
        """Writes to csv file result of sorting mails."""
        with open(filename, "w", encoding="utf-8") as resul_file:
            writer = csv.writer(resul_file, lineterminator="\r")
            for key, emails in self.categories.items():
                for email in emails:
                    row = [key, email]
                    writer.writerow(row)
        logger.info(f"The sorter '{self.name}' writes result of sorting to file {result_file}")

    def sort_mails(self):
        """This method sorts mails in categories depends on decision method."""
        if self.list_of_mails:
            while self.list_of_mails:
                new_mail = self.list_of_mails.pop()
                decisions = self.decision(new_mail)
                if decisions:
                    for dec in decisions:
                        self.categories[dec].append(new_mail)
                else:
                    self.categories["Others"].append(new_mail)
            logger.info(f"The sorter '{self.name}' already ended sorting mails.")

    def decision(self, text_of_mail: str) -> tuple:
        """Takes mail, parse it and returns tuple of categories(max: 3) as decision."""
        str_list = re.split(r'\W+', text_of_mail)[:-1]
        res_dict = {el: 0 for el in CATEGORIES}
        for word in str_list:
            for category, keywords in self.knowledge.items():
                for keyword in keywords:
                    if keyword.lower() in word.lower():
                        res_dict[category] += 1
        res_list = sorted(res_dict.items(), key=lambda x: x[1], reverse=True)[:2]
        return tuple(el[0] for el in res_list if el[1] > 2)

    def return_result(self):
        print("-" * 170)
        for category, mails in self.categories.items():
            print(f"\n\nCATEGORY {category}:\n\n")
            for mail in mails:
                print(mail, end="\n\n")
            print("-" * 170)
        print("THE END")
        logger.info(f"The sorter '{self.name}' returns result of sorting in console.")


if __name__ == "__main__":
    new_segregator = MailSegregator("sorter", *CATEGORIES)
    new_segregator.read_mails_file(file_name)
    new_segregator.sort_mails()
    new_segregator.write_result_to_file(result_file)
    # new_segregator.return_result()
