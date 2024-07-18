from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

board = ['' for _ in range (9)]
current_player = 'X'

def check_win():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], #Check rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Check columns
        [0, 4, 8], [2, 4, 6] #Check diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != '':
            return True
    return False

def check_draw():
    return '' not in board
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    global board, current_player
    data = request.get_json()
    index = data['index']

    if board[index]  == '' and not check_win():
        board[index] == current_player
        if check_win():
            return jsonify({'status': 'win', 'player': current_player})
        elif check_draw():
            return({'status': 'draw'})
        else:
            current_player = 'O' if current_player == 'X'   else 'X'
            return jsonify({'status': 'continue', 'player': current_player})
    return jsonify({'status': 'invalid'})

@app.route('/reset', methods=['POST'])
def reset():
    global board, current_player
    board= ['' in range(9)]
    current_player = 'X'
    return jsonify({'status': 'reset'})

if __name__ == '__main__':
    app.run(debug=True)