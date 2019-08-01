#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Replace "pass" with your code

class BankAccount(object):
    def __init__(self,label,balance):
        self.label = label
        self.balance = balance

    def __str__(self):
        return self.label + ":" + str(self.balance)

    
#WITHDRAW FUNCTION
    def withdraw(self,balance):
        if balance < 0:
            print "cannot withdraw negative amounts"
        elif balance > self.balance:
            print "cannot withdraw more than you have"
        else:
            self.balance = self.balance - 1

    
#WITHDRAW FUNCTION
    def deposit(self,balance):
        if balance < 0:
            print "cannot deposit negative amounts"
        else:
            self.balance = self.balance + balance

    def rename(self,label):
        if not label == "":
            self.label = label
    


