def draw_custom_pattern(rows,columns):
    ref=columns
    #print(ref)
    for i in range(rows):
        for _ in range(columns):
            if i <=0:
                print(" ___    ",end="")
        print()


        for _ in range(columns):

            if _ <ref-1:
                #print(j)
                print("/   \\___", end="")
            else:
                print("/   \\", end="")
        print()

    #print the last row
        for _ in range(columns):
            print("\\___/   ", end="")
        #print()

def main():
    rows = int(input("Enter the number of rows:"))
    column = int(input("Enter the number of columns"))
    column = column+rows-column
    draw_custom_pattern(rows, column)

if __name__ == "__main__":
    main()
