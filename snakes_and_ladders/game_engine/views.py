from django.shortcuts import render, HttpResponse

# Create your views here.
def no_js(request):
    return render(request, "game_engine/no_js.html")

def basic_grid(request):
    return render(request, "game_engine/basic_grid.html")    

def all_server_side(request):
    # Board constraints
    # Head > tail
    # Head and tail should be in range(2,99)
    board_details={
    'snakes':[
        {
            'snake1':{'head':'val','tail':'val'}
        },
        {
            'snake2':{'head':'val','tail':'val'}
        }
    ],
    'ladders':[
        {
            'ladder1':{'head':'val','tail':'val'}
        },
        {
            'ladder2':{'head':'val','tail':'val'}
        }
    ]
    }
    return HttpResponse("Holla")

def test(request):
    return render(request, 'game_engine/game_canvas.html')