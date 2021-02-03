import os
from typing import List
from .search import SearchFile


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class DirectoryVisualiser(object):
    """
    visualises the directory
    """
    def __init__(self, directory_path: str, include_hidden: bool, query: str):
        """
        :param directory_path: <str> 
        :param include_hidden: <bool>
        """
        self.directory_path = directory_path
        self.include_hidden = include_hidden
        self.query = query

    def list_contents(self, directory_path: str) -> List[str]:
        """
        lists the folder's contents ignoring folders that start with "__" e.g.: __pycache__

        :param directory_path: <str> the current directory to look into 
        :return: List[str] an array containing the contents of the directory
        """
        contents = os.listdir(directory_path)

        dir_contents = list()
        file_contents = list()
        for ind, content in enumerate(contents):
            if content.startswith(".") and not self.include_hidden:
                continue
            elif content.startswith("__"):
                continue
            if os.path.isdir(directory_path + "/" + content):
                dir_contents.append(content)
            else:
                file_contents.append(content)
        return file_contents + dir_contents
    
    @staticmethod
    def __fix_directory_ending(directory: str):
        """
        :param directory: <str> path to directory
        """
        return directory if directory.endswith("/") else directory + "/"

    def recursive_search(self, directory_path, root_directory, query):
        """
        for content in directory:
            if content is directory:
                directory -> directory + content
                redo
            else print(content)

        :param directory_path:
        :param root_directory:
        """
        directory_path = self.__fix_directory_ending(directory_path)
        for content in self.list_contents(directory_path):
            if os.path.isdir(directory_path + "/" + content):
                print("[ROOT DIR: ]/" + (self.__fix_directory_ending(directory_path) + content).split(root_directory)[1]) 
                print("         |\n          ---")
                self.recursive_search(directory_path + content, root_directory, query)
            else:
                directory_path = self.__fix_directory_ending(directory_path)
                if directory_path == root_directory:
                    match_counter = SearchFile(directory_path + content, query).search()
                    if match_counter > 0:
                        color = bcolors.OKGREEN
                    else:
                        color = ""
                    match_message = ' [matches found: {}]'.format(match_counter)
                    print(content + color + match_message + bcolors.ENDC)
                else:
                    match_counter = SearchFile(directory_path + content, query).search()
                    if match_counter > 0:
                        color = bcolors.OKGREEN
                    else:
                        color = ""
                    print("             " * directory_path.split(root_directory)[1].count("/") + content, 
                         color + " [matches found: {}]".format(match_counter) + bcolors.ENDC)


    def visualise(self):
        self.directory_path = self.directory_path if self.directory_path.endswith("/") else self.directory_path + "/"
        self.recursive_search(self.directory_path, self.directory_path, self.query)
