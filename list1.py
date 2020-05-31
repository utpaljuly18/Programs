{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the namesac\n",
      "This is not my pet\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the nameutpal\n",
      "This is not my pet\n"
     ]
    }
   ],
   "source": [
    "myPets = ['Zophie', 'sweety','cutie','pichku']\n",
    "#print(\"Enter the pet name :\")\n",
    "name = input(\"Enter the name\")\n",
    "if name not in myPets:\n",
    "    print(\"This is not my pet\")\n",
    "else:\n",
    "    print(\"This is my pet\",name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the namesweety\n",
      "yes sweety\n"
     ]
    }
   ],
   "source": [
    "name = input(\"Enter the name\")\n",
    "def mypets(list):\n",
    "    if name not in list:\n",
    "        print(\"No\")\n",
    "    else:\n",
    "        print(\"yes\",name)\n",
    "mypets(list(['Zophie', 'sweety','cutie','pichku']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "7\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "list = [5,7,9,8]\n",
    "for i in list:\n",
    "    if i % 2 != 0:\n",
    "        print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 3, 5, 7, 9]\n",
      "[2, 4, 6, 8, 10]\n"
     ]
    }
   ],
   "source": [
    "list = [1,2,3,4,5,6,7,8,9,10]\n",
    "n1 = []\n",
    "n2 = []\n",
    "for i in list:\n",
    "    if i % 2 != 0:\n",
    "        n1.append(i)\n",
    "    else:\n",
    "        n2.append(i)\n",
    "print(n1)\n",
    "print(n2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 5]\n"
     ]
    }
   ],
   "source": [
    "list1 = [1,3,5,6]\n",
    "list2 = [1,2,5,4]\n",
    "n = []\n",
    "p1 = 0\n",
    "p2 = 0\n",
    "\n",
    "while p1 < len(list1) and p2 < len(list2):\n",
    "    if list1[p1] == list2[p2]:\n",
    "        n.append(list1[p1])\n",
    "        p1 += 1\n",
    "        p2 += 1\n",
    "    elif list1[p1] > list2[p2]:\n",
    "        p2 += 1\n",
    "    else:\n",
    "        p1 += 1\n",
    "print(n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['a', 'A', 'B', 'c']\n"
     ]
    }
   ],
   "source": [
    "spam = ['B','a','A','c']\n",
    "spam.sort(key = str.lower)\n",
    "print(spam)"
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
