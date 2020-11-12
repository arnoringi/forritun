#definition for music_func goes here
def music_func(music='Classic Rock', group='The Beatles', singer='Freddie Mercury'):
    print("The best type of music is:", music)
    print("The best music groups is:", group)
    print("The best lead vocalist is:", singer)


def main():
    music, group, singer = input("Input music, group, singer: ").split(',')
    music_func(music, group, singer)
    music_func()

main()