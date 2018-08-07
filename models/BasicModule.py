# coding: utf-8
# Author: Zhongyang Zhang

import torch
import torch.nn as nn
import torch.optim as optim
import time 


class BasicModule(nn.Module):
    def __init__(self):
        super(BasicModule,self).__init__()
        self.model_name = self.__class__.__name__
    
    def load(self, path):
        checkpoint = torch.load(path)
        epoch      = checkpoint['epoch']
        best_acc   = checkpoint['best_acc']
        self.load_state_dict(checkpoint['state_dict'])
        return self, epoch, best_acc

    def save(self, epoch, test_acc, name=None):
        prefix   = "./source/trained_net/" + self.model_name + "/"
        if name is None:
            name = "temp_model.dat"
        path     = prefix + name 

        torch.save({
            'epoch': epoch + 1,
            'state_dict': self.state_dict(),
            'best_acc': test_acc,
        }, path)
        return path

    def get_optimizer(self, lr):
        optimizer = optim.Adam(self.parameters(), lr=lr)
        return optimizer


