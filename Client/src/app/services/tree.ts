import * as d3 from 'd3';

export class Tree {
    constructor() { }

    // Tree configuration
    private branches = [];
    private seed = { i: 0, x: 50, y: 100, a: 0, l: 10, d: 0 }; // a = angle, l = length, d = depth
    private da = 0.3; // Angle delta
    private dl = 0.85; // Length delta (factor)
    private ar = 0.7; // Randomness
    private maxDepth = 10;

    private color = d3.scaleLinear()
        .domain([1, this.maxDepth])
        .range(["black", "green"]);


    // Tree creation functions
    branch(b) {
        var end = this.endPt(b), daR, newB;

        this.branches.push(b);

        if (b.d === this.maxDepth)
            return;

        // Left branch
        daR = this.ar * Math.random() - this.ar * 0.5;
        newB = {
            i: this.branches.length,
            x: end.x,
            y: end.y,
            a: b.a - this.da + daR,
            l: b.l * this.dl,
            d: b.d + 1,
            parent: b.i
        };
        this.branch(newB);

        // Right branch
        daR = this.ar * Math.random() - this.ar * 0.5;
        newB = {
            i: this.branches.length,
            x: end.x,
            y: end.y,
            a: b.a + this.da + daR,
            l: b.l * this.dl,
            d: b.d + 1,
            parent: b.i
        };
        this.branch(newB);
    }

    public regenerate(initialise, svg) {
        this.branches = [];
        this.branch(this.seed);
        initialise ? this.create(svg) : this.update(svg);
    }

    endPt(d) {
        // Return endpoint of branch
        const x = d.x + d.l * Math.sin(d.a);
        const y = d.y - d.l * Math.cos(d.a);
        return { x: x, y: y };
    }

    // D3 functions
    x1(d) { return d.x; }
    y1(d) { return d.y; }
    x2(d) { return (d.x + d.l * Math.sin(d.a)); }
    y2(d) { return (d.y - d.l * Math.cos(d.a)); }

    create(svg) {
        const color = this.color;
        svg.selectAll('line')
            .data(this.branches)
            .enter()
            .append('line')
            .attr('x1', this.x1)
            .attr('y1', this.y1)
            .attr('x2', this.x2)
            .attr('y2', this.y2)
            .style('stroke-width', function (d) {
                var t = parseInt("" + (this.maxDepth * .5 + 1 - d.d * .5));
                return t + 'px';
            })
            .style('stroke', function (d) {
                return color(d.d);
            })
            .attr('id', function (d) { return 'id-' + d.i; });
    }

    update(svg) {
        svg.selectAll('line')
            .data(this.branches)
            .transition()
            .attr('x1', this.x1)
            .attr('y1', this.y1)
            .attr('x2', this.x2)
            .attr('y2', this.y2);
    }
}
