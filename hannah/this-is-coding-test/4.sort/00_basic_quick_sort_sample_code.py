# 퀵 정렬
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(pivot)로 설정
# 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나
# 병합 정렬과 더불어 대부분 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘(파이썬도 병합, 퀵 하이브리드 정렬)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
# pivot 값은 5
# 왼쪽에서부터는 피벗값보다 큰 데이터를 고른다
# 오른쪽에서부터는 피벗값보다 작은 데이터를 고른다
# 즉, 5를 제외하고 7부터 쭉 보면서 5보다 큰 데이터를 찾는다. 여기서는 바로 7이 나오기 때문에 끝
# 그리고 8부터 쭉 왼쪽으로 오면서 5보다 작은 데이터를 찾는다. 여기서는 두번째 탐색에서 4를 찾을 수 있다.
# 그리고나서 7과 4의 위치를 바꿔준다.

# 위 과정을 반복한다.
# 그러다가 피벗값보다 큰 값과 피벗값보다 작은 값의 위치가 엇갈렸을 때는 (예를 들어 5, 4, 2, 0, 3, 1, 6, 9, 7, 8인 상황) 작은 값(1)과 피벗값(5)의 위치를 바꿔준다. 
# 그러면  4, 2, 0, 3, 1, 5, 6, 9, 7, 8이 된다. 포인트는 5를 기준으로 5보다 앞에 있는 값들은 5보다 작은 수들이 모이게 되고, 5보다 뒤에 있는 값들은 5보다 큰 수들이 모인다.
# 여기까지 하면 "분활 완료" 상태다.
# 그러고나서 피벗값을 기준으로 왼쪽에 있는 데이터들끼리 퀵정렬 알고리즘을 수행하고(이때 피벗은 이 데이터들 중 가장 첫번째 데이터), 오른쪽에 있는 데이터들끼리도 퀵정렬 알고리즘을 수행한다()
# 이처럼 퀵 정렬 알고리즘은 재귀적으로 수행된다.

# 평균적으로 O(NlogN)의 시간 복잡도를 갖는다.
# 하지만 최악의 경우에는 O(N²)의 시간 복잡도를 갖는다.(하지만 표준 라이브러리에서는 이러한 점을 개선해서 짜여저 있어서 최소 O(NlogN)을 보장한다)
# 최악의 경우는 이미 정렬된 상태이다. 


def quick_sort(array, start_index, end_index):
    if start_index >= end_index:  # 원소가 1개인 경우 바로 종료
        return
    
    pivot = start_index  # 피벗은 첫번째 원소로 설정한다
    left = start_index + 1
    right = end_index
    
    while (left <= right):  # 엇갈릴때까지 반복
        
        # 피벗보다 큰 데이터를 찾을 때까지 반복 
        while (left <= end_index and array[left] <= array[pivot]):
            left += 1

        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while (right > start_index and array[right] >= array[pivot]):
            right -= 1
        
        if (left > right):  # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start_index, right - 1)
    quick_sort(array, right + 1, end_index)


quick_sort(array, 0, len(array) - 1)
print(array)