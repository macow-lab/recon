from flask import Flask, request, render_template, Response, Blueprint
from flask_login import login_required, current_user
from database import Database

class Networth:
    def __init__(self):
        self.__assets = {}
        self.__passives = {}
        self.__networth = None

    def getAsset(self):
        return self.__assets


    def setAsset(self, assets: dict):
        self.__assets = assets
        return self.__assets


    def getPassives(self):
        return self.__passives


    def setPassives(self, passives: dict):
        self.__passives = passives
        return self.__passives


    def calculateNetworth(self):
        for value in self.__assets.values():
            self.__networth += value

        for value in self.__passives.values():
            self.__passives -= value

        return self.__networth