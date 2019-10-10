class Array
    def stalin_sort_arr(array)
        max = array[0]
        array.select do |item|
            max > item ? next : max = item
        end
    end

    def stalin_sort
        return [] if empty?

        max = first
        select do |x|
            next if max > x
            max = x
            xmax > y; max = y
        end
    end

    # ブロックあり
    def stalin_sort_by(&block)
        return [] if empty?

        max = yield(first)
        map { |x| [yield(x), x] }
        .select { |y, _x| next if max > y; max = y }
        .map { |_y, x| x }
    end
end