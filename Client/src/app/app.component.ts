import { Component, ViewChild, ElementRef, OnInit, NgZone } from '@angular/core';
import { Square } from './square';

@Component({
  selector: 'app-root',
  template: `
    <canvas #canvas width="1500" height="800"></canvas>
    <button (click)="play()">Play</button>
  `,
  styles: ['canvas { border-style: solid; margin-top: 3em; margin-left: 5em}']
})
export class AppComponent implements OnInit {
  @ViewChild('canvas', { static: true }) canvas: ElementRef<HTMLCanvasElement>;
  ctx: CanvasRenderingContext2D;
  ln: CanvasRenderingContext2D;
  grass: CanvasRenderingContext2D;
  anthill: CanvasRenderingContext2D;

  requestId;
  interval;
  squares: Square[] = [];

  cantAnts = 30

  constructor(private ngZone: NgZone) {}

  ngOnInit() {
    this.ctx = this.canvas.nativeElement.getContext('2d');
    this.ln = this.canvas.nativeElement.getContext('2d');
    this.grass = this.canvas.nativeElement.getContext('2d');
    this.anthill = this.canvas.nativeElement.getContext('2d');
    
    this.ngZone.runOutsideAngular(() => this.tick());
    setInterval(() => {
      this.tick();
    }, 200);
  }

  tick() {
    this.ctx.clearRect(0, 0, this.ctx.canvas.width, this.ctx.canvas.height);
    this.squares.forEach((square: Square) => {
      square.moveRight();
    });
    this.requestId = requestAnimationFrame(() => this.tick);

    this.ln.beginPath();       // Start a new path
    this.ln.lineWidth = 4;
    this.ln.strokeStyle = 'brown'
    this.ln.moveTo(1050, 500);    
    this.ln.lineTo(1050, 700);

    this.ln.strokeStyle = 'brown'
    this.ln.moveTo(1150, 500);    
    this.ln.lineTo(1150, 700);

    this.ln.strokeStyle = 'brown'
    this.ln.moveTo(1250, 500);   
    this.ln.lineTo(1250, 700);

    this.ln.strokeStyle = 'brown'
    this.ln.moveTo(1350, 500);  
    this.ln.lineTo(1350, 700);
    
    this.ln.stroke();

    this.grass.beginPath();
    this.grass.lineWidth = 4;
    this.grass.strokeStyle = 'green'

    this.grass.moveTo(200, 700);
    this.grass.lineTo(1400, 700);

    this.grass.moveTo(200, 750);
    this.grass.lineTo(1400, 750);
    this.grass.stroke();


    this.anthill.beginPath();
    this.anthill.ellipse(100, 700, 50, 50, Math.PI / 4, 0, 2 * Math.PI);
    this.anthill.strokeStyle = 'black';
    this.anthill.fillStyle = 'black';
    this.anthill.stroke();
    
    
  }

  play() {
    
    const square = new Square(this.ctx);
    for(let i = 0; i < 1; i++)
      this.squares = this.squares.concat(square);
  }

  ngOnDestroy() {
    clearInterval(this.interval);
    cancelAnimationFrame(this.requestId);
  }
}