
# This script takes the current tool directory
# clones it to another folder with the same parent directory
# renames all the instances of the current ToolName with the prompted new name
# searches through files and replaces in there as well

$PARENT_DIRECTORY = (Get-Item -Path "..\").FullName
$NEW_TOOL_NAME = Read-Host -Prompt 'New Tool Name'
$NEW_TOOL_FOLDER = $PARENT_DIRECTORY + "\" + $NEW_TOOL_NAME
$CURRENT_FOLDER = $PSScriptRoot
$CURRENT_TOOL_NAME = "TOOL_NAME"

echo "New Tool Name: $NEW_TOOL_NAME"
echo ""


# Clone to new folder
Copy-Item -Path $CURRENT_FOLDER -Recurse -Destination $NEW_TOOL_FOLDER -Container


# Remove .git folder
Get-ChildItem -Path $NEW_TOOL_FOLDER\.git -Recurse | Remove-Item -force -recurse
Remove-Item $NEW_TOOL_FOLDER\.git -Force 


# Rename files in folder
Get-ChildItem $NEW_TOOL_FOLDER -recurse | 
Foreach-Object {
    if ($_.Name -like '*' + $CURRENT_TOOL_NAME + '*') {
        Rename-Item -Path $_.PSPath -NewName $_.Name.replace($CURRENT_TOOL_NAME, $NEW_TOOL_NAME)
    }
    
}

# Find instances of TOOL_NAME in files and replace them with the new tool name
Get-ChildItem $NEW_TOOL_FOLDER -recurse -File | 
Foreach-Object {
    
    $_.FullName
    
    ((Get-Content -path $_.FullName -Raw) -replace $CURRENT_TOOL_NAME, $NEW_TOOL_NAME) | Set-Content -Path $_.FullName
    
}

echo ""
echo "New Tool: '$NEW_TOOL_NAME' created"


# pause before exit
cmd /c pause | out-null