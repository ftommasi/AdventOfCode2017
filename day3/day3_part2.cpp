#include <iostream>
#include <math>

using namespace std;

int main(){
  int target;
  cin >> target;
  
  int grid_sqrt = ((int)sqrt(target)) + 1;
  int grid_size = 1;
  int row_col_size = 1;
  int tile_value = 0;
  
  row_col_size = (grid_sqrt % 2 == 0 ? grid_sqrt + 1 : grid_sqrt);
  grid_size = row_col_size * row_col_size;
  int grid[row_col_size][row_col_size];

  //initialize grid to all -1
  for(int i=0; i < row_col_size; i++){
    for(int j=0; j < row_col_size; j++){
      grid[i][j] = -1;
    }
  }

  int i_marker = row_col_size/2;
  int j_marker = row_col_size/2;

  //first move is to the right. i +=1; j+=0
  int next_i_modifier = 1;
  int next_j_modifier = 0;
  
  grid[i_marker][j_marker] = 1
  

}
