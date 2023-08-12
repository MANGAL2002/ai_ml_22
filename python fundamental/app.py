{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as ttk\n",
    "from tkinter import font\n",
    "app=ttk.Tk()\n",
    "app.title('attendance system')\n",
    "app.geometry('600x400')\n",
    "font_=font.Font(size=20)\n",
    "ttk.Label(app,text='face recognition based attendance system ',font=font_).pack()\n",
    "def register():\n",
    "    print('register')\n",
    "def attendence():\n",
    "    print('attendance')\n",
    "def clear_data():\n",
    "    print('clear all previous data')\n",
    "ttk.Button(app,text='register',command=register,font=font_).pack()\n",
    "ttk.Button(app,text='attendance',command=attendence,font=font_).pack()\n",
    "ttk.Button(app,text='clear_data',command=clear_data,font=font_).pack()\n",
    "app.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.5"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
