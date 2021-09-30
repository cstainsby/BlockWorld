from BlockWorld import BlockWorld

def main():
    """
    Driver for Block World
    """
    blockWorld = BlockWorld()

    totalRuns = blockWorld.run()

    print("Block World finished in " + str(totalRuns) + " totalRuns")
    

if __name__ == '__main__':
    main()