import torch
from torch import nn
class MultiHorizonLSTM(nn.Module):
 def __init__(self,input_size,horizon=7,hidden=64):
  super().__init__()
  self.h=horizon
  self.lstm=nn.LSTM(input_size,hidden,batch_first=True)
  self.fc=nn.Linear(hidden,horizon)
 def forward(self,x):
  o,_=self.lstm(x)
  return self.fc(o[:,-1,:])
