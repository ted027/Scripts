def stalin_sort(array)
    max = array[0]
    array.select do |item|
        max > item ? next : max = item
    end
end

print(stalin_sort ['a', 'c', 'b', 'a','c','d'])
print(stalin_sort [1, 2, 10, 3, 4, 5, 15, 6, 30, 20])