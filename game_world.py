# 게임 월드 관히 모듈

# 게임 월드의 표현
# 두개의 layer를 갖는 게임월드로 구현
objects = [ [], [], [] ] # [object], [layer]


# 월드에 객체를 넣는 함수
def add_object(o, depth = 0):
    objects[depth].append(o)


# 월드를 업데이트 하는, 객체들을 모두 업데이트하는 함수
def update():
    for layer in objects:  # 오브젝트의 레이어를 업데이트
        for o in layer:  # 레이어안의 모든 객체들을 업데이트
            o.update()


# 월드 객체들을 모두 그리기
def render():
    for layer in objects:  # 오브젝트의 레이어를 업데이트
        for o in layer:
            o.draw()


# 객체 삭제
def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            return  # 이미 지웠으니까 루프를 반복할 필요가 없음.

    raise ValueError('invaild object remove')