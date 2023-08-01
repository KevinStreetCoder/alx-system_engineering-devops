#!/usr/bin/env ruby

# Check if there is an argument provided
if ARGV.empty?
	puts "Usage: #{$PROGRAM_NAME} <string>"
	exit(1)
      end
      
      # Regular expression method to match the word "School"
      def match_school(string)
	regex = /School/
	matches = string.scan(regex)
	matches.empty? ? '' : matches.join('')
      end
      
      # Accept the argument and call the method to match "School"
      input_string = ARGV[0]
      result = match_school(input_string)
      puts result
      