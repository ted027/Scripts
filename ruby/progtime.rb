def time
    sum = 0
    while sum >= 0
        puts "学習時間を入力してください"
        line = "--------------------------"
        time = gets.to_f
        sum += time

        puts <<~EOS
            今月#{sum}時間勉強したよ！
            #{line}
            残り時間は#{100 - sum}です
            #{line}
            今月の想定学習時間の#{sum / 100 * 100}%勉強しました
            #{line}
        EOS
    end
end

time