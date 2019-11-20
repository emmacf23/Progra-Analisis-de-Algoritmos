export class Tree {
    private color = 'black';
    private x = 0;
    private y = 750;
    private z = 8;
  
    constructor(private ctx: CanvasRenderingContext2D) {}
  
    moveRight() {
      this.x++;
      this.draw();
    }
  
    private draw() {
      this.ctx.fillStyle = this.color;
      this.ctx.fillRect(this.z * this.x, this.z * this.y, this.z, this.z);
    }
  }
  