plot3(0, 0, 0, 'o', 1, 1, 1, 'o', 'color',[0 0 0], 'LineWidth', 2);

hold on
plot3(2, 2, 0, 'o', 3, 3, 0, 'o', 'color',[0 0 0], 'LineWidth', 2);
hold off

x1 = [0, 1];
y1 = [0, 1];
z1 = [0, 1];

hold on
plot3(x1, y1, z1, 'k-', 'color',[0 0 0], 'LineWidth', 2);
hold off

p7 = [2, 2, 0];
p8 = [3, 3, 0];

hold on
plot([p7(1) p8(1)], [p7(2) p8(2)], 'color',[0 0 0], 'LineWidth', 2);
hold off

grid on
grid minor

xlabel('X axis','fontweight','bold')
ylabel('Y axis','fontweight','bold')
zlabel('Z axis','fontweight','bold')