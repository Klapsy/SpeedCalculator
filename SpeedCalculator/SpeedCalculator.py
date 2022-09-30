tempo = int(input('Tempo (bpm): ')) #Tempo input
notetype = int(input('There is a list of note types.\n1. 1/8      5. 1/8  - 3:2/6:4       9. 1/8  - 5:4/10:8     \
13. 1/8  - 7:4\n2. 1/16     6. 1/16 - 3:2/6:4      10. 1/16 - 5:4/10:8     14. 1/16 - 7:4\n3. 1/32     \
7. 1/32 - 3:2/6:4      11. 1/32 - 5:4/10:8     15. 1/32 - 7:4\n4. 1/64     8. 1/64 - 3:2/6:4      \
12. 1/64 - 5:4/10:8     16. 1/64 - 7:4\nPick one and type your choice: ')) #Note value input
if notetype == 1: #Calculation cascade
    tempo /=30
    print('The speed is', tempo, 'notes per second.')
elif notetype == 2:
    tempo /=15
    print('The speed is', tempo, 'notes per second.')
elif notetype == 3:
    tempo /=7.5
    print('The speed is', tempo, 'notes per second.')
elif notetype == 4:
    tempo /=3.75
    print('The speed is', tempo, 'notes per second.')
elif notetype == 5:
    tempo /=20
    print('The speed is', tempo, 'notes per second.')
elif notetype == 6:
    tempo /=10
    print('The speed is', tempo, 'notes per second.')
elif notetype == 7:
    tempo /=5
    print('The speed is', tempo, 'notes per second.')
elif notetype == 8:
    tempo /=2.5
    print('The speed is', tempo, 'notes per second.')
elif notetype == 9:
    tempo /=24
    print('The speed is', tempo, 'notes per second.')
elif notetype == 10:
    tempo /=12
    print('The speed is', tempo, 'notes per second.')
elif notetype == 11:
    tempo /=6
    print('The speed is', tempo, 'notes per second.')
elif notetype == 12:
    tempo /=3
    print('The speed is', tempo, 'notes per second.')
elif notetype == 13:
    tempo = tempo / 60 * 2 * 1.75
    print('The speed is', tempo, 'notes per second.')
elif notetype == 14:
    tempo = tempo / 60 * 4 * 1.75
    print('The speed is', tempo, 'notes per second.')
elif notetype == 15:
    tempo = tempo / 60 * 8 * 1.75
    print('The speed is', tempo, 'notes per second.')
elif notetype == 16:
    tempo = tempo / 60 * 16 * 1.75
    print('The speed is', tempo, 'notes per second.')
else:
    print('You did something wrong... So please')
