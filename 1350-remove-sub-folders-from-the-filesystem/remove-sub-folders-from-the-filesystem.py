class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # sort with the length of the string
        new_folder = []
        for item in folder:
            new_folder.append((len(item), item))
        new_folder.sort()

        # use set to check if start with the folder
        folder_set = set()
        for length, folders in new_folder:
            idx = 1
            while idx < len(folders):
                if folders[idx] == "/" and folders[:idx] in folder_set:
                    break
                idx += 1
            else:
                folder_set.add(folders)
        return list(folder_set)