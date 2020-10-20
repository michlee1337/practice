class Leader():
    def __init__(self):
        self.online = True
        self.chunkservers = {} # chunkservers[id] = chunkserver_object ## workaround!
        self.file_to_chunk = {}  # file_md[file_id] = [chunkserverid1, ... chunkserveridn]
        self.chunk_version = {} # chunk_md[chunk_id] = chunk_ver
        self.chunkserver_primary = {} # chunk_md[chunk_id] = primary_chunkserver_id
        self.chunk_location = {} # chunk_md[chunk_id] = ((server1, loc1), ..., (server1, loc3))
        self.chunkserver_load = {} # chunkserver_load[chunkserver_id] = number_of_chunks

    def append_chunk(self): # fill in the parameters
        # get the chunkservers with lowest load
        # update metadata
        # send append chunk request to primary chunkserver !! make sure to send _all_ necessary information
        pass

    def respond_to_chunkserver_down(self,lost_chunkserver_id):
        # hello good luck :) ping me for help
        pass


class ChunkServer():
    def __init__(self, id):
        # self.online = True
        self.id = id
        self.chunk_version = {} # chunk_md[chunk_id] = chunk_ver
        self.memory = [] # dummy disk memory xD
        self.last_location = 0 # store "location" index of next writable location

    # note: skipping the optimization of chunkserver chaining

    def append_as_primary(self): # fill in the parameters
        # write to own memory and update metadata
        # send append request to backup replicas.
        pass

    def append_as_backup(self): # fill in the parameters
        # write to own memory and update metadata
        # send append request to next backup replica if any.
        pass

def __main__():
    leader = Leader()
    server1 = ChunkServer(1)
    server2 = ChunkServer(2)
    server3 = ChunkServer(3)
    server4 = ChunkServer(4)
    leader.chunkservers[1] = server1
    leader.chunkservers[2] = server2
    leader.chunkservers[3] = server3
    leader.chunkservers[4] = server4

    # store some dummy data in them
    # update the leader metadata to match
    # store everything in GFS()

    # check leader metadata
    # make a specific chunkserver fail
    # assert that metadata still has three replicas for the affected chunks
    # assert that the chunkservers cited for those chunks are not the failed chunkserver
    # assert that the affected chunks are in the memory where the leader says they are
