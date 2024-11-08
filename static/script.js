function toggleFolder(folderName) {
    var folderContent = document.getElementById('folder-' + folderName);
    if (folderContent.style.display === 'none') {
        folderContent.style.display = 'block';
    } else {
        folderContent.style.display = 'none';
    }
}