# the Hello Classs

class Hello
	
	def initialize( name )
		@name = name.capitalize
	end

	def salute
		puts "Hello #{@name}!"
	end

end

# create a new object
h = Hello.new("Ruby")

h.salute