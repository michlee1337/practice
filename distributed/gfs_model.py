class GFSModel():
    def __init__():
        self.leader = None
        self.chunkservers = []

        # im skipping logs and shadowleaders because omg

        self.show_actions = False

    def chunkserver_failure():
        pass

    def master_failure():
        pass

    def run():
        while True:
            # chunkserver

class Log():
    def __init__():
        self.online = True
        pass

class Leader():
    def __init__():
        self.online = True
        self.file_to_chunk = {}  # file_md[file_id] = [chunkserverid1, ... chunkserveridn]
        self.chunk_version = {} # chunk_md[chunk_id] = chunk_ver
        self.chunkserver_primary = {} # chunk_md[chunk_id] = primary_chunkserver_id
        self.chunk_location = {} # chunk_md[chunk_id] = ((server1, loc1), ..., (server1, loc3))
        self.chunkserver_load = {} # chunkserver_load[chunkserver_id] = number_of_chunks

    def append_chunk():
        # get the chunkservers with lowest load
        # update metadata
        # send append chunk request to primary chunkserver
        pass

class ChunkServer():
    def __init__():
        self.online = True
        pass

    def heartbeat():
        # tell leader its ok
        pass

    def

class Chunk():
    def __init__():
        self.online = True
        pass

    def __main__():
        pass
