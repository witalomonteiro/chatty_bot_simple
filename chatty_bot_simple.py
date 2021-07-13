{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "chatty_bot_simple",
      "provenance": [],
      "authorship_tag": "ABX9TyNFbwFbTnS2ozh73n8A8C2a",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/witalomonteiro/chatty_bot_simple/blob/main/chatty_bot_simple.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rzNM8stJbR2t",
        "outputId": "c1ae8c0b-1610-4286-d4b9-d440518eb0b6"
      },
      "source": [
        "print(28 % 3)\n",
        "print(28 % 5)\n",
        "print(28 % 7)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "1\n",
            "3\n",
            "0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "npRft5R0WYgb",
        "outputId": "1538e054-244b-4578-ca61-4e495235a028"
      },
      "source": [
        "bot_name = 'Pandemia'\n",
        "birth_year = '2020'\n",
        "your_name = ''\n",
        "\n",
        "print(f'''Hello! My name is {bot_name}.\n",
        "I was created in {birth_year}.''')\n",
        "\n",
        "print('Please, remind me your name.')\n",
        "your_name = input()\n",
        "\n",
        "print(f'What a great name you have, {your_name}!')\n",
        "\n",
        "print('''Let me guess your age.\n",
        "Enter remainders of dividing your age by 3, 5 and 7.''')\n",
        "remainder3 = int(input())\n",
        "remainder5 = int(input())\n",
        "remainder7 = int(input())\n",
        "your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105\n",
        "print(f\"Your age is {your_age}; that's a good time to start programming!\")\n",
        "\n",
        "print('Now I will prove to you that I can count to any number you want.')\n",
        "number = int(input())\n",
        "i = 0\n",
        "while i <= number:\n",
        "    print(f\"{i} !\")\n",
        "    i += 1\n",
        "\n",
        "print(\"\"\"\n",
        "Let's test your programming knowledge.\n",
        "Why do we use methods?\n",
        "1. To repeat a statement multiple times.\n",
        "2. To decompose a program into several small subroutines.\n",
        "3. To determine the execution time of a program.\n",
        "4. To interrupt the execution of a program.\"\"\")\n",
        "answer = int(input())\n",
        "while answer != 2:\n",
        "    print(\"Please, try again.\")\n",
        "    answer = int(input())\n",
        "print(\"Completed, have a nice day!\")\n",
        "\n",
        "print(\"Congratulations, have a nice day!\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Hello! My name is Pandemia.\n",
            "I was created in 2020.\n",
            "Please, remind me your name.\n",
            "Witalo Monteiro\n",
            "What a great name you have, Witalo Monteiro!\n",
            "Let me guess your age.\n",
            "Enter remainders of dividing your age by 3, 5 and 7.\n",
            "3\n",
            "4\n",
            "5\n",
            "Your age is 54; that's a good time to start programming!\n",
            "Now I will prove to you that I can count to any number you want.\n",
            "10\n",
            "0 !\n",
            "1 !\n",
            "2 !\n",
            "3 !\n",
            "4 !\n",
            "5 !\n",
            "6 !\n",
            "7 !\n",
            "8 !\n",
            "9 !\n",
            "10 !\n",
            "\n",
            "Let's test your programming knowledge.\n",
            "Why do we use methods?\n",
            "1. To repeat a statement multiple times.\n",
            "2. To decompose a program into several small subroutines.\n",
            "3. To determine the execution time of a program.\n",
            "4. To interrupt the execution of a program.\n",
            "3\n",
            "Please, try again.\n",
            "4\n",
            "Please, try again.\n",
            "2\n",
            "Completed, have a nice day!\n",
            "Congratulations, have a nice day!\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}