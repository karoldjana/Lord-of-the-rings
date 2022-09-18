from src.lotr_sdk import LotrSdk

def error_message():
    print(" ### ERROR!: You paste an incorrect character identifier. ### \n") 


def select_action():
    print('__________________________________________________________________________________')
    print("""
    WELCOME TO LORD OF THE RINGS SDK\n
    Select the action you want to take by pressing a number on your keyboard:
    1. List all of "The Lord of the Rings" books.
    2. Request one specific book.
    3. Request all chapters of one specific book.
    4. Get a list of all movies, including the "The Lord of the Rings" and the "The Hobbit" trilogies.
    5. Request one specific movie.
    6. Request all movie quotes for one specific movie (only working for the LotR trilogy).
    7. List of characters including metadata like name, gender, realm, race and more.
    8. Request one specific character.
    9. Request all movie quotes of one specific character.
    10. List of all movie quotes.
    11. Request one specific movie quote.
    12. List of all book chapters.
    13. Request one specific book chapter.
    """)
    print('__________________________________________________________________________________')
   

while True:
    select_action()
    user_input = int(input())
    api_key = "ERuGLVktHDZsNg9Edo9I"
    lotr = LotrSdk(api_key)

    if user_input==1:
        print(" ### Getting all books... ### \n")
        all_books_json = lotr.get_all_books()
        all_books_info = all_books_json['docs']
        print(all_books_info)
        print("\n ### Do you want to get a list of the book names and identifiers? (y/n) ### ")
        user_input = input()
        if(user_input=="y"):
            print("List of books' names and identifiers: ")
            num = 1
            for info in all_books_info:
                print("{} - Book name: ".format(num) + info['name'] + ". Book id: "+ info['_id'])
                num+=1

    elif user_input==2:
        print(""" ### Some examples of books. Select a book identifier, copy and paste it:  ### 
        1 - Book id: 5cf5805fb53e011a64671582
        2 - Book id: 5cf58077b53e011a64671583
        3 - Book id: 5cf58080b53e011a64671584
        """)
    
        user_input=input()
        if(len(user_input)==24):
            print(" ### Getting a specific book... ### \n")
            book_json = lotr.get_a_book(user_input)
            book_info = book_json['docs']
            print(book_info)
            print("\n ### Do you want to get a list of the book information? (y/n) ### ")
            user_input = input()
            if(user_input=="y"):
                print(" ### List of the book's information  ### ")
                num = 1
                for info in book_info:
                    print("{} - Book name: ".format(num) + info['name'] + ". Book id: "+ info['_id'])
                    num+=1
        else:
            error_message()  

    elif user_input==3:
        print(""" ### Some examples of books. Select a book identifier, copy and paste it:  ### 
        1 - Book id: 5cf5805fb53e011a64671582
        2 - Book id: 5cf58077b53e011a64671583
        3 - Book id: 5cf58080b53e011a64671584
        """)
        user_input=input()
        if(len(user_input)==24):
            print(" ### Getting all chapters from the book selected... ### \n")
            chapters_from_book = lotr.get_chapters_from_book(user_input)
            chapters = chapters_from_book['docs']
            print(chapters)  

            print("\n ### Do you want to get a clean list of the book chapters? (y/n) ### ")
            user_input = input()
            if(user_input=="y"):
                print(" ### List of books' chapters:  ### ")
                num = 1
                for info in chapters:
                    print("{} - Book chapter: ".format(num) + info['chapterName'] + ". Chapter id: "+ info['_id'])
                    num+=1  
        else:
            error_message()          

    elif user_input==4:
        print(" ### Getting all movies... ### \n")
        movies_json = lotr.get_all_movies()
        movies = movies_json['docs']
        print(movies)  
        print("\n ### Do you want to get a clean list of the movies' info? (y/n) ### ")
        user_input = input()
        if(user_input=="y"):
            print(" ### List of movies:  ### ")
            num = 1
            for info in movies:
                print("{} - Movie name: ".format(num) + info['name'] + ". Budget(Mill): {}".format(info['budgetInMillions']) +
                ". Academy Award Nominations: {}".format(info['academyAwardNominations']) + ". Movie id: "+ info['_id'])
                num+=1    

    elif user_input==5:
        print(""" ### Some examples of movies. Select a movie identifier, copy and paste it:  ### 
        1 - Movie id: 5cd95395de30eff6ebccde56
        2 - Movie id: 5cd95395de30eff6ebccde57
        3 - Movie id: 5cd95395de30eff6ebccde584
        """)
        user_input=input()
        if(len(user_input)==24):
            print(" ### Getting a specific movie... ### \n")
            movie_json = lotr.get_a_movie(user_input)
            movie_info = movie_json['docs']
            print(movie_info)
            print("\n ### Do you want to get a list of the movie information? (y/n) ### ")
            user_input = input()
            if(user_input=="y"):
                print(" ### List of the movie's information:  ### ")
                num = 1
                for info in movie_info:
                    print("{} - Movie name: ".format(num) + info['name'] + ". Movie id: "+ info['_id'])
                    num+=1    
        else:
            error_message()        

    elif user_input==6:
        print(""" ### Some examples of movies. Select a movie identifier, copy and paste it:  ### 
        1 - Movie id: 5cd95395de30eff6ebccde56
        2 - Movie id: 5cd95395de30eff6ebccde57
        3 - Movie id: 5cd95395de30eff6ebccde584
        """)
        user_input=input()
        if(len(user_input)==24):
            print(" ### Getting all quotes from the movie selected... ### \n")
            quotes_from_movies_json = lotr.get_a_movies_quotes(user_input)
            quotes_from_movies = quotes_from_movies_json['docs']
            print(quotes_from_movies_json)  
        else:
            error_message()    

    elif user_input==7:
        print(" ### Getting all characters... ### \n")
        characters_json = lotr.get_all_characters() 
        all_characters = characters_json['docs']
        print(all_characters)
        
        print("\n ### Do you want to get a list of the characters info? (y/n) ### ")
        user_input = input()
        if(user_input=="y"):
            print(" ### List of characters info:  ### ")
            num = 1
            for info in all_characters:
                print("{} - Name: ".format(num) + info['name'] + ". Race: "+ info['race']
                + ". Gender: "+ info['gender'] + ". Id: "+ info['_id'])
                num+=1

    elif user_input==8:
        print(""" ### Some examples of characters id. Select a character identifier, copy and paste it:  ### 
        1 - Char id: 5cd99d4bde30eff6ebccfbc2
        2 - Char id: 5cd99d4bde30eff6ebccfbbf
        3 - Char id: 5cd99d4bde30eff6ebccfbc0
        """)
        print(" ### Getting a specific character... ### \n")
        user_input = input()
        character_json = lotr.get_a_character(user_input)

        character = character_json['docs']
        print(character)
        
        print("\n ### Do you want to get a list of the character info? (y/n) ### ")
        user_input = input()
        if(user_input=="y"):
            print(" ### List of character's info:  ### ")
            num = 1
            for info in character:
                print("{} - Name: ".format(num) + info['name'] + ". Race: "+ info['race']
                + ". Gender: "+ info['gender'] + ". Id: "+ info['_id'])
                num+=1
    
    elif user_input==9:
        print(""" ### Some examples of characters id. Select a character identifier, copy and paste it:  ### 
        1 - Char id: 5cd99d4bde30eff6ebccfc15
        2 - Char id: 5cd99d4bde30eff6ebccfca7
        3 - Char id: 5cd99d4bde30eff6ebccfe9e
        """)
        user_input=input()
        if(len(user_input)==24):
            print(" ### Getting all quotes from the character selected... ### \n")
            quotes_from_char_json = lotr.get_all_char_quotes(user_input)
            quotes = quotes_from_char_json['docs']
            print(quotes)  
            print("\n ### Do you want to get a clean list of their quotes? (y/n) ### ")
            user_input = input()
            if(user_input=="y"):
                print(" ### List of quotes:  ### ")
                num = 1
                for info in quotes:
                    print("{} - Quote: ".format(num) + info['dialog'] + ". Character: "+ info['character'])
                    num+=1 
        else:
            error_message()
              

    elif user_input==10:
        print(" ### Getting all quotes... ### \n")
        movie_quotes_json = lotr.get_all_movie_quotes() 
        all_quotes = movie_quotes_json['docs']
        print(all_quotes)
        
        print("\n ### Do you want to get a list of all quotes? (y/n) ### ")
        user_input = input()
        if(user_input=="y"):
            print(" ### List of quotes:  ### ")
            num = 1
            for info in all_quotes:
                print("{} - Quote: ".format(num) + info['dialog'] + ". Quote id: "+ info['id'])
                num+=1   

    elif user_input==11:
        print(""" ### Some examples of quotes id. Select a quote identifier, copy and paste it:  ### 
        1 - Quote id: 5cd96e05de30eff6ebcce841
        2 - Quote id: 5cd96e05de30eff6ebcce835
        3 - Quote id: 5cd96e05de30eff6ebcce831
        """)
    
        user_input=input()
        if(len(user_input)==24):
            print(" ### Getting a quote info... ### \n")
            movie_quote_json = lotr.get_movie_quote(user_input)
            quote = movie_quote_json['docs']
            print(quote)
            print("\n ### Do you want to get quote info? (y/n) ### ")
            user_input = input()
            if(user_input=="y"):
                print(" ### List of the quote's information  ### ")
                num = 1
                for info in quote:
                    print("{} - Quote: ".format(num) + info['dialog'] + ". Id: "+ info['id'])
                    num+=1
        else:
            error_message()  
    
    elif user_input==12:
        print(" ### Getting all chapters... ###\n")
        all_chapters_from_book = lotr.get_all_chapters()
        all_chapters = all_chapters_from_book['docs']
        print(all_chapters)
        
        print("\n ### Do you want to get a list of all chapters? (y/n) ###")
        user_input = input()
        if(user_input=="y"):
            print("###List of quotes: ###")
            num = 1
            for info in all_chapters:
                print("{} - Chapter: ".format(num) + info['chapterName'] + ". Book: "+ info['book'] 
                + ". Chapter id: "+ info['_id'])
                num+=1   
    
    elif user_input==13:
        print(""" ### Some examples of chapters id. Select a chapter identifier, copy and paste it: ###
        1 - Chapter id: 6091b6d6d58360f988133bba
        2 - Chapter id: 6091b6d6d58360f988133bc0
        3 - Chapter id: 6091b6d6d58360f988133bc3
        """)
    
        user_input=input()
        if(len(user_input)==24):
            print("### Getting a chapter info... ###\n")
            chapter_from_book_json = lotr.get_book_chapter(user_input)
            chapter = chapter_from_book_json['docs']
            print(chapter_from_book_json)
            print("\n### Do you want to get clean quote info? (y/n) ###")
            user_input = input()
            if(user_input=="y"):
                print("### List of the chapters' information ###")
                num = 1
                for info in chapter:
                    print("{} - Chapter: ".format(num) + info['chapterName'] + ". Chapter id: "+ info['_id'])
                    num+=1
        else:
            error_message()  

    else:
        print("### See you soon! ###\n")
        break