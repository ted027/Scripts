def stalin_sort(array)
    max = array[0]
    array.select do |item|
        max > item ? next : max = item
    end
end
