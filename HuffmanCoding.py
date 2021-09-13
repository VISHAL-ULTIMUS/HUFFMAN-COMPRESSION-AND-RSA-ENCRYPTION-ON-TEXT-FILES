# -*- coding: utf-8 -*-


from HuffmanCompressor import HuffmanCompressor
from HuffmanDecomporessor import HuffmanDecompressor

class Huffman(object):

    def __init__(self, files, huffman_file):



        self.files = files
        self.huffman_file = huffman_file

    def compress(self):

        exec_time = 0
        compressor = HuffmanCompressor(self.huffman_file)

        # To override the file if it exists
        open(self.huffman_file, "w").close()

        with open(self.huffman_file, "ab") as f:
            ba = len(self.files).to_bytes(4, byteorder="little")
            f.write(ba)

        for path, file_ in self.files.items():
            exec_time += compressor.compress(file_, path)

        return exec_time

    def decompress(self):
        
        decompressor = HuffmanDecompressor(self.huffman_file)
        return decompressor.decomp()
