import * as THREE from "three";
import { OrbitControls as e } from "three/addons/controls/OrbitControls.js";
import * as BufferGeometryUtils from "three/addons/utils/BufferGeometryUtils.js";
import { SUBTRACTION as t, Brush as n, Evaluator as r } from "three-bvh-csg";

!(function () {
  "use strict";
  function a() {
    ((E = new THREE.Scene()).environment = w),
      (l = new THREE.WebGLRenderer({
        canvas: canvas,
        antialias: !0,
        alpha: !0
      })).setPixelRatio(window.devicePixelRatio),
      l.setSize(window.innerWidth, window.innerHeight),
      (l.useLegacyLights = !1),
      (s = new THREE.PerspectiveCamera(
        35,
        window.innerWidth / window.innerHeight,
        0.1,
        3 * H
      )).position.set(0, 0, H * Math.sqrt(2)),
      s.lookAt(0, 0, 0);
    const a = new THREE.AmbientLight(16777215, 0.3);
    E.add(a);
    const u = new THREE.DirectionalLight(16777215, 1);
    u.position.set(0, 2 * H, 0),
      E.add(u),
      (E.fog = new THREE.FogExp2(16101802, 0.005)),
      (m = new THREE.MeshStandardMaterial({
        metalness: 1,
        roughness: 0
      })),
      (p = []),
      (c = c = new THREE.CapsuleGeometry(3, 6, 5, 20)).rotateZ(-Math.PI / 3.78),
      c.translate(0, -1, 0),
      c.scale(1, 1, 0.85),
      c.scale(0.24, 0.24, 0.24),
      (c = (function (e) {
        let a,
          o,
          i,
          s,
          E = e.clone(),
          l = new THREE.MeshBasicMaterial({}),
          d = 2 * c.parameters.radius,
          m = 2 * c.parameters.height,
          h = new THREE.BoxGeometry(d, m, d);
        return (
          h.translate(-d / 2, 0, 0),
          (a = new r()),
          (o = new n(E, l)),
          (i = new n(h, l)),
          (a.useGroups = !0),
          (s = a.evaluate(o, i, t, s)).geometry
        );
      })(c)),
      p.push(c),
      (c = c.clone()).rotateY(Math.PI),
      p.push(c),
      (c = BufferGeometryUtils.mergeGeometries(p)),
      (c = BufferGeometryUtils.mergeVertices(c)).computeVertexNormals();
    const M = new THREE.Color(),
      T = new THREE.Matrix4();
    h = new THREE.InstancedMesh(c, m, R);
    for (let e = 0; e < R; e++)
      g(T),
        h.setMatrixAt(e, T),
        h.setColorAt(
          e,
          M.setHSL(
            Math.abs(THREE.MathUtils.randInt(9750, 1e4) / 1e4),
            1,
            THREE.MathUtils.randInt(450, 700) / 1e3
          )
        );
    E.add(h);
    (c = new THREE.SphereGeometry(0.3, 20, 10)),
      (m = m.clone()).color.set("deeppink"),
      (m.roughness = 0.3),
      (h = new THREE.InstancedMesh(c, m, 220));
    for (let e = 0; e < 220; e++) g(T), h.setMatrixAt(e, T);
    E.add(h),
      ((d = new e(s, l.domElement)).autoRotate = !0),
      (d.enableDamping = !0),
      (d.enablePan = !1),
      (d.minDistance = 0.1),
      (d.maxDistance = H * Math.sqrt(2)),
      (d.minPolarAngle = 0),
      (d.maxPolarAngle = Math.PI / 2),
      d.target.set(0, 0, 0),
      d.update(),
      window.addEventListener("resize", o),
      i();
  }
  function o() {
    (s.aspect = window.innerWidth / window.innerHeight),
      s.updateProjectionMatrix(),
      l.setSize(window.innerWidth, window.innerHeight);
  }
  function i() {
    requestAnimationFrame(i), d.update(), l.render(E, s);
  }
  let s,
    E,
    l,
    d,
    c,
    m,
    h,
    w,
    u,
    p = [];
  const R = 700,
    H = 50,
    g = (function () {
      const e = new THREE.Vector3(),
        t = new THREE.Euler(),
        n = new THREE.Quaternion(),
        r = new THREE.Vector3();
      return function (a) {
        (e.x = (2 * Math.random() - 1) * H),
          (e.y = (2 * Math.random() - 1) * H),
          (e.z = (2 * Math.random() - 1) * H),
          (t.x = 0),
          (t.z = 2 * Math.random() * Math.PI),
          (t.y = 2 * Math.random() * Math.PI),
          n.setFromEuler(t),
          r.set(1, 1, 1),
          a.compose(e, n, r);
      };
    })();
  (u = new THREE.TextureLoader()).setCrossOrigin(""),
    u.load(
      "https://happy358.github.io/Images/HDR/kloofendal_48d_partly_cloudy_puresky_2k.jpg",
      function (e) {
        (e.colorSpace = THREE.SRGBColorSpace),
          (e.minFilter = THREE.NearestFilter),
          (e.generateMipmaps = !1),
          (e.mapping = THREE.EquirectangularReflectionMapping),
          (w = e),
          a();
      }
    );
})();
