import json
import os

class FileController:
    links = {}
    def __init__(self):
        self.filename = 'links.json'
        FileController.links = FileController.links

    def process_json(self):
        """
        Processes the json file as a python dictionary for O(1) lookup
        """
        if os.path.isfile(self.filename):
            links_file = open(self.filename).read()
            FileController.links = json.loads(links_file)
        else:
            open(self.filename, 'w')
            FileController.links = {}

    def print_uploads(self):
        """
        Prints each video title that has been uploaded 
        """
        self.process_json()
        print 'Uploaded videos:'
        for title in FileController.links:
            print title

    def return_link(self, title):
        """
        Returns the link that is mapped from the passed in title
        Return None if the title is NOT in the dictionary
        Args:
            title: a string that represents the desired video title
        """
        if title in FileController.links:
            return 'https://www.youtube.com/watch?' + FileController.links[title]
        return None

    def write_link(self, name, link):
        """
        Writes a video filename and link to the file associated
        with this object

        Args:
            name: A string representing the file name
            link: A string representing the youtube link
        """
        FileController.links[name] = link
        with open(self.filename, 'w') as fp:
            json.dump(FileController.links, fp)

    def remove_link(self, title):
        """
        Removes the specified video from the json file and dict

        Args:
            title: The title string
        """
        if title in FileController.links:
            del FileController.links[title]
            print 'Removed ' + title
        else:
            print title + ' not found'

    def clear_links(self):
        """
        Clears everything in the json and dict
        """
        FileController.links = {}
        with open(self.filename, 'w') as fp:
            json.dump(FileController.links, fp)
    