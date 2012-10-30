# Latex compiling script
# Uses guard-shell gem

guard :shell, all_on_start: true do
    # watch all tex source files
    watch /.*tex$/ do |m|
        puts "Compiling..."
        # Compile modified source
        `pdflatex -interaction=batchmode #{m[0]} && echo "Compiled!"`

        # Cleanup
        `rm *.aux *.log`
    end
end
