require 'pry'

def start_libraries(libraries)
  puts libraries
end

def avarage_books_score(books)
  sum = 0

  books.each do |book|
    sum += book.values.first.to_i
  end

  sum.to_f / books.size
end

def extract_and_sort_books(scores, all_books_scores)
  books = scores.map do |s|
    { "book-#{s}" => all_books_scores[s] }
  end

  books.sort_by(&:values).reverse
end

def start(filename)
  file = File.open(filename)
  content = file.read.split("\n")

  nr_of_books, nr_of_libraries, max_days = content[0].split(' ')
  all_books_scores = content[1].split(' ')

  libraries = {}

  index = 0
  content.drop(2).each_slice(2) do |group|
    nr_of_books, signup_days, bpd = group[0].split(' ')
    scores = group[1].split(' ').collect {|s| s.to_i }

    sorted_books = extract_and_sort_books(scores, all_books_scores)

    libraries[index] = {
      nr_of_books: nr_of_books,
      signup_days: signup_days,
      books_per_day: bpd,
      books: sorted_books,
      avarage_score: avarage_books_score(sorted_books)
    }

    index += 1
  end

  start_libraries(libraries)

  file.close
end

start(ARGV.first)
