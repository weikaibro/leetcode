class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        new_folder = []
        for item in folder:
            new_folder.append((len(item), item))
        new_folder.sort()
        # print(new_folder)

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