plot3(0, 0, 0, 'o', 0, -1, 0, 'o', 'color',[0 0 0], 'LineWidth', 2);
hold on
plot3(1, 0, 0, 'o', 1, -2, 0, 'o', 'color',[0 0 0], 'LineWidth', 2);
hold off

hold on
plot3(0, 2, 0, 'o', 0, 3, 0, 'o', 'color',[0 0 0], 'LineWidth', 2);
hold off

hold on
plot3(-1, 2, 0, 'o', -1, 3, 0, 'o', 'color',[0 0 0], 'LineWidth', 2);
hold off

p1 = [0, 0];
p2 = [0, -1];
p4 = [1, 0];
p3 = [1, -2];
p5 = [0, 2];
p6 = [0, 3];
p8 = [-1, 2];
p7 = [-1, 3];

hold on
plot([p3(1) p4(1)], [p3(2) p4(2)], 'color',[0 0 0], 'LineWidth', 2);
hold off

hold on
plot([p5(1) p6(1)], [p5(2) p6(2)], 'color',[0 0 0], 'LineWidth', 2);
hold off

hold on
plot([p6(1) p7(1)], [p6(2) p7(2)], 'color',[0 0 0], 'LineWidth', 2);
hold off

hold on
plot([p7(1) p8(1)], [p7(2) p8(2)], 'color',[0 0 0], 'LineWidth', 2);
hold off

hold on
plot([p8(1) p5(1)], [p8(2) p5(2)], 'color',[0 0 0], 'LineWidth', 2);
hold off

xlabel('X axis','fontweight','bold')
ylabel('Y axis','fontweight','bold')
zlabel('Z axis','fontweight','bold')

grid on
grid minor